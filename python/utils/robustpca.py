import fbpca
import numpy as np


class RobustPCA:
    """Implementation of Robust PCA using the Inexact ALM algorithm.

    Args:
        tol: Tolerance for convergence. Default value is 1e-9.
        max_iters: Maximum number of iterations. Default value is 3.

    """

    def __init__(self, tol: float = 1e-9, max_iters: int = 3):
        self.tol = tol
        self.max_iters = max_iters

    def converged(self, z: np.array, d_norm: float) -> bool:
        """Check if the algorithm has converged.

        Args:
            z: Residual matrix.
            d_norm: Frobenius norm of the original matrix.

        Returns:
            True if converged, False otherwise.

        """
        err = np.linalg.norm(z, 'fro') / d_norm
        print('error: ', err)
        return err < self.tol

    @staticmethod
    def shrink(m: np.array, tau: float):
        """Perform shrinkage operation on the matrix.

        Args:
            m: Input matrix.
            tau: Shrinkage value.

        Returns:
            Resulting matrix after shrinkage.

        """
        s = np.abs(m) - tau
        return np.sign(m) * np.where(s > 0, s, 0)

    @staticmethod
    def _svd(m: np.array, rank: int) -> tuple:
        """Perform truncated singular value decomposition.

        Args:
            m: Input matrix.
            rank: Rank of decomposition.

        Returns:
            Tuple with matrices U, S, and V.

        """
        return fbpca.pca(m, k=min(rank, np.min(m.shape)), raw=True)

    def norm_op(self, m: np.array) -> float:
        """Calculate the operator norm of the matrix.

        Args:
            m: Input matrix.

        Returns:
             Operator norm value.

        """
        return self._svd(m, 1)[1][0]

    def svd_reconstruct(self, m: np.array, rank: int, min_sv: float) -> tuple:
        """Perform reconstruction via truncated SVD.

        Args:
            m: Input matrix.
            rank: Rank of decomposition.
            min_sv: Minimum singular value.

        Returns:
            Tuple with the reconstructed matrix and the number of non-zero
                singular values.

        """
        u, s, v = self._svd(m, rank)
        s -= min_sv
        nnz = (s > 0).sum()
        return u[:, :nnz] @ np.diag(s[:nnz]) @ v[:nnz], nnz

    def pcp(self, x: np.array, max_iter: int = 10, k: int = 10) -> tuple:
        """Perform Robust PCA.

        Args:
            x: Input matrix.
            max_iter: Maximum number of iterations. Default is 10.
            k: Parameter k. Default is 10.

        Returns:
            Tuple with the low-rank matrix, the sparse matrix, and intermediate
                examples.

        """
        m, n = x.shape
        trans = m < n
        if trans:
            x = x.T
            m, n = x.shape

        lamda = 1 / np.sqrt(m)
        op_norm = self.norm_op(x)
        y = np.copy(x) / max(op_norm, np.linalg.norm(x, np.inf) / lamda)
        mu = k * 1.25 / op_norm
        mu_bar = mu * 1e7
        rho = k * 1.5

        d_norm = np.linalg.norm(x, 'fro')
        l = np.zeros_like(x)
        sv = 1

        examples = []

        for i in range(max_iter):
            print("rank sv:", sv)
            x2 = x + y / mu

            # update estimate of sparse matrix by "shrinking/truncating":
            # original - low-rank
            s = self.shrink(x2 - l, lamda / mu)

            # update estimate of low-rank matrix by doing truncated SVD of
            # rank sv & reconstructing
            # count of singular values > 1/mu is returned as svp
            l, svp = self.svd_reconstruct(x2 - s, sv, 1 / mu)

            # If svp < sv, you are already calculating enough singular values.
            # If not, add 20% (in this case 240) to sv
            sv = svp + (1 if svp < sv else round(0.05 * n))

            # residual
            z = x - l - s
            y += mu * z
            mu *= rho

            examples.extend([s[140, :], l[140, :]])

            if m > mu_bar:
                m = mu_bar
            if self.converged(z, d_norm):
                break

        if trans:
            l = l.T
            s = s.T
        return l, s, examples