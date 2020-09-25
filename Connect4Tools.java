// Tiffany McBrayer 
// Connect 4 conference project 

import javax.swing.*;
import java.awt.*; //Graphics, Graphics2D, Color
import java.awt.geom.*; //Ellipse2D, Rectangle2D, Line2D, Arc2D 
import java.util.*; // Arrays, ArrayList
import java.awt.event.*;


public class Connect4Tools {
  
       // Connect4Tools.checkForFour(matrix, 'Y');
       // for debugging purposes
       public static void main(String[] args) {
           char [][] matrix = new char [] [] {{' ',' ',' ',' ',' ',' ',' '},
                                   {' ',' ',' ',' ',' ',' ',' '},
                                   {' ',' ',' ','R',' ',' ',' '},
                                   {'R',' ','Y',' ','R',' ',' '},
                                   {'R',' ','Y',' ',' ','R',' '},
                                   {'R',' ','Y',' ',' ',' ','R'}};
           
           // 7 rows, 6 colms
           System.out.println(checkForFour(matrix, 'Y'));
           for (int i = 0; i < 6; i++) {
                System.out.println(Arrays.toString(matrix[i]));
           }
         
       }
  
      // checking rows in matrix
      public static boolean rowWin(char[][] matrix, int row, int col, char symbol) {
          for (int i = 0; i < 4; i++) { 
               if (inBounds(row, col) != true) {
                   return false; 
               } else { 
                   if (matrix[row][col] != symbol) {
                       return false;
                   }
               }
               col++;
          } 
          return true;
      }
      
      // checking columns in matrix
      public static boolean columnWin(char[][] matrix, int row, int col, char symbol) {
          for (int i = 0; i < 4; i++) {
              if (inBounds(row, col) != true) {
                  return false; 
              } else { 
                  if (matrix[row][col] != symbol) {
                      return false;
                  }
              }
              row++;
          }
          return true;
      }
      
      // checking right diagonal in matrix
      public static boolean upRightDiagonalWin(char[][] matrix, int row, int col, char symbol) {
          for (int i = 0; i < 4; i++) {
              if (inBounds(row, col) != true) {
                  return false; 
              } else { 
                  if (matrix[row][col] != symbol) {
                      return false;
                  }
                  row--;
                  col++;
              }
          }
          return true;
      }
      
      // checking left diagonal in matrix
      public static boolean upLeftDiagonalWin(char[][] matrix, int row, int col, char symbol) {
          for (int i = 0; i < 4; i++) {
              if (inBounds(row, col) != true) {
                  return false; 
              } else { 
                  if (matrix[row][col] != symbol) {
                      return false;
                  }
                  row--;
                  col--;
              }
          }
          return true;
      }
      
      // making sure the points checking are in bounds
      public static boolean inBounds(int row, int col) {
          int numRows = 6;
          int numCols = 7;
          if (row >= numRows) {
              return false; 
          } else if (row < 0) {
              return false;
          } else if (col >= numCols) {
              return false;
          } else if (col < 0) {
              return false;
          }
          return true; 
      }
      
      // check all 4 ways in matrix
      public static boolean checkForFour(char[][] matrix, char symbol) {
          for (int r = 0; r < 6; r++) {
               for (int c = 0; c < 7; c++) {
                    if (rowWin(matrix, r, c, symbol) == true) {
                        return true;
                    }else if (columnWin(matrix, r, c, symbol) == true) {
                        return true;
                    }else if (upRightDiagonalWin(matrix, r, c, symbol) == true) {
                        return true;
                    }else if (upLeftDiagonalWin(matrix, r, c, symbol) == true) {
                        return true;
                    }
               }
          }
          return false;
      } 
      
}