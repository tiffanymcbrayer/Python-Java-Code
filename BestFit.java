import java.io.*;
import java.util.Arrays;  
//best fit line 

public class BestFit {
  
    public static void main(String[] args) {
      
      double[][] point = {{2,1},{5,2},{7,3},{8,3}};
      
      double [][] matrix = bestFitP1(point);
      
      
      System.out.println("matrix that needs to be put into reduced echelon form");
      for (int i = 0; i < matrix.length; i++) {
           System.out.println(Arrays.toString(matrix[i]));
      }

      //double [][] points2 = {{1,0,(2.0/7)},{0,1,(5.0/14)}};
      //double [][] matrix2 = bestFitP2(points2);
      
      /*
      // for testing purposes
      System.out.println("matrix");
      for (int i = 0; i < matrix2.length; i++) {
           System.out.println(Arrays.toString(matrix2[i]));
      }
      */
      System.out.println("Best fit line");
      //System.out.printf("y = %.4f + %.4fx\n", matrix2[0][0], matrix2[1][0]);


    }
    
    public static double [][] bestFitP1(double[][] points) {
        double[][] a = new double[points.length][2];
        for (int i = 0; i < points.length; i++) {
            a[i][0] = 1;
            a[i][1] = points[i][0];
        }
        double[][] b = new double[points.length][1];
        for (int i = 0; i < points.length; i++) {
             b[i][0] = points[i][1];
        }
        double[][] aT = new double[2][points.length];
        for (int i = 0; i < points.length; i++) {
            aT[0][i] = 1;
            aT[1][i] = points[i][0];
        }
        double [][] aTtimesA = matrixMutl(aT,a);
        double [][] aTtimesB = matrixMutl(aT,b);
        double[][] newMatrix = new double[aTtimesA.length][aTtimesA[0].length+1];
        for (int i = 0; i < aTtimesA.length; i++) {
            for (int j = 0; j < aTtimesA[0].length; j++) {
                 newMatrix[i][j] = aTtimesA[i][j];
            }
        }
        for (int i = 0; i < aTtimesB.length; i++) {
            newMatrix[i][aTtimesA[0].length] = aTtimesB[i][0];
        }
        return newMatrix;
      
    } // going to return a matrix ready to be reduced
    
    
    public static double[][] bestFitP2(double[][] matrix) {
        double [][] newMatrix = new double[matrix.length][1];
        for (int i = 0; i < matrix.length; i++) {
             newMatrix[i][0] = matrix[i][matrix[0].length-1];
        }
        return newMatrix;
    }
    
    
    public static double[][] matrixMutl(double[][] m1, double[][] m2) {
        double [][] newMatrix = new double[m1.length][m2[0].length];
        if (m1[0].length == m2.length) {
          for (int i = 0; i < m1.length; i++) { // rows of first matrix
              for (int j = 0; j < m2[0].length; j++) {  // col of first matrix
                  for (int k = 0; k < m2.length; k++) { // rows of second matrix
                       newMatrix[i][j] += m1[i][k] * m2[k][j];
                  }
              }        
           }      
        }
        return newMatrix;
    }
}
        
        