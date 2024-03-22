#include <stdio.h>
#include <gsl/gsl_linalg.h>

int main() {
    // Define the matrix
    double matrix_data[] = {3.0, -1.0, 1.0, 
                            3.0, 6.0, 2.0, 
                            3.0, 3.0, 7.0};
    
    // Define the right-hand side vector
    double rhs_data[] = {1.0, 0.0, 4.0};
    
    // Define the dimensions of the matrix
    size_t size = 3;
    
    // Allocate memory for matrix and vector
    gsl_matrix_view mat = gsl_matrix_view_array(matrix_data, size, size);
    gsl_vector_view rhs = gsl_vector_view_array(rhs_data, size);
    
    // Allocate memory for permutation matrix and LU decomposition
    gsl_permutation *p = gsl_permutation_alloc(size);
    
    // Perform LU decomposition
    int signum;
    gsl_linalg_LU_decomp(&mat.matrix, p, &signum);
    
    // Solve the system of linear equations
    gsl_vector *x = gsl_vector_alloc(size);
    gsl_linalg_LU_solve(&mat.matrix, p, &rhs.vector, x);
    
    // Verify correctness by reconstructing the original matrix
    gsl_matrix *reconstructed_mat = gsl_matrix_alloc(size, size);
    gsl_matrix *L = gsl_matrix_alloc(size, size);
    gsl_matrix *U = gsl_matrix_alloc(size, size);
    gsl_matrix_set_identity(L);
    
    // Get L and U matrices
    for (size_t i = 0; i < size; i++) {
        for (size_t j = 0; j < size; j++) {
            if (i > j) {
                gsl_matrix_set(L, i, j, gsl_matrix_get(&mat.matrix, i, j));
            } else {
                gsl_matrix_set(U, i, j, gsl_matrix_get(&mat.matrix, i, j));
            }
        }
    }
    
    // Reconstruct the original matrix using L and U
    gsl_blas_dgemm(CblasNoTrans, CblasNoTrans, 1.0, L, U, 0.0, reconstructed_mat);
    
    // Print the reconstructed matrix
    printf("Reconstructed Matrix LU:\n");
    for (size_t i = 0; i < size; i++) {
        for (size_t j = 0; j < size; j++) {
            printf("%8.3f ", gsl_matrix_get(reconstructed_mat, i, j));
        }
        printf("\n");
    }
    
    // Free allocated memory
    gsl_permutation_free(p);
    gsl_vector_free(x);
    gsl_matrix_free(reconstructed_mat);
    gsl_matrix_free(L);
    gsl_matrix_free(U);
    
    return 0;
}

/* out put 

L:
   {1.000  ,  0.000,    0.000, 
   1.000  ,   1.000,    0.000 ,
   1.000  ,  0.500  ,  1.000 }



U:
  { 3.000 ,  -1.000,    1.000, 
   0.000,    7.000,    1.000, 
   0.000,    0.000,    3.500} 


reconstructed_mat:
   {3.000,   -1.000,    1.000, 
   3.000,    6.000,    2.000, 
   3.000,    3.000,    7.000} 


   */
