// Tiffany McBrayer 
// Connect 4 conference project 

import javax.swing.*;
import java.awt.*; //Graphics, Graphics2D, Color
import java.awt.geom.*; //Ellipse2D, Rectangle2D, Line2D, Arc2D 
import java.util.*; // Arrays, ArrayList
import java.awt.event.*;

public class Connect4 extends JFrame{
  
    // instance variables
    private ArrayList<Rectangle2D.Double> squares;
    private ArrayList<ArrayList<Ellipse2D.Double>> blankTiles;  
    private char [][] matrix;
    private Color tileColor;
    private char symbol;
    private int columnNumTile;
    private int rowNumTile;
    private int player = 1;
    private String winner = "none";
    private char play = 'g';
    private int yellowWins = 0;
    private int redWins = 0;
    
    // -------------------------------------------------------------------------------
    
    private class ListenerForKeys implements KeyListener {
        int m1 = 5, m2 = 5, m3 = 5, m4 = 5, m5 = 5, m6 = 5, m7 = 5; // row counters
        public void keyPressed(KeyEvent event) {
            if (play == 's') {
                for (int i = 0; i < 6; i++) {
                     for (int j = 0; j < 7; j++) {
                          matrix[i][j] = ' ';
                     }
                }
                m1 = 5; m2 = 5; m3 = 5; m4 = 5; m5 = 5; m6 = 5; m7 = 5;
                play = 'g';
            }
            if (event.getKeyCode() == 49) {
              if (play != 's'){
                if (m1 >= 0) {
                    if (player == 1) {
                        matrix[m1][0] = 'R';
                        m1--;
                    } else {
                        matrix[m1][0] = 'Y';
                        m1--;
                    }
                }
              }
            } if (event.getKeyCode() == 50) {
                if (play != 's'){
                if (m2 >= 0) {
                    if (player == 1) {
                        matrix[m2][1] = 'R';
                        m2--;
                    } else {
                        matrix[m2][1] = 'Y';
                        m2--;
                    }
                }
                }
            } if (event.getKeyCode() == 51) {
              if (play != 's'){
                if (m3 >= 0) {
                    if (player == 1) {
                        matrix[m3][2] = 'R';
                        m3--; 
                    } else {
                        matrix[m3][2] = 'Y';
                        m3--; 
                    }
                }
              }
            } if (event.getKeyCode() == 52) {
              if (play != 's'){
                if (m4 >= 0) {
                    if (player == 1) {
                        matrix[m4][3] = 'R';
                        m4--;
                    } else {
                        matrix[m4][3] = 'Y';
                        m4--;
                    }
                }
              }
            } if (event.getKeyCode() == 53) {
              if (play != 's'){
                if (m5 >= 0) {
                    if (player == 1) {
                        matrix[m5][4] = 'R';
                        m5--;
                    } else { 
                        matrix[m5][4] = 'Y';
                        m5--;
                    }
                }
              }
            } if (event.getKeyCode() == 54) {
              if (play != 's'){
                if (m6 >= 0) {
                    if (player == 1) {
                        matrix[m6][5] = 'R';
                        m6--;
                    } else { 
                        matrix[m6][5] = 'Y';
                        m6--;
                    }
                }
              }
            } if (event.getKeyCode() == 55) {
              if (play != 's'){
                if (m7 >= 0) {
                    if (player == 1) {
                        matrix[m7][6] = 'R';
                        m7--;
                    } else { 
                        matrix[m7][6] = 'Y';
                        m7--;
                    }
                }
              }
           } if (event.getKeyCode() == 67) {
                for (int i = 0; i < 6; i++) {
                     for (int j = 0; j < 7; j++) {
                          matrix[i][j] = ' ';
                     }
                }
                m1 = 5; m2 = 5; m3 = 5; m4 = 5; m5 = 5; m6 = 5; m7 = 5;
                play = 'g';
           }
           if (player == 1) {
               player = 2;
           } else {
               player = 1;
           }
            
           if (Connect4Tools.checkForFour(matrix, 'R') == true) {
               System.out.println("Red won!");
               winner = "red";
               redWins++;
               System.out.println("Red has " + redWins + " wins");
               System.out.println("Yellow has " + yellowWins + " wins");
               System.out.println();
               play = 's';
           } else if (Connect4Tools.checkForFour(matrix, 'Y')) {
               winner = "yellow";
               System.out.println("Yellow won!");
               yellowWins++;
               System.out.println("Red has " + redWins + " wins");
               System.out.println("Yellow has " + yellowWins + " wins");
               System.out.println();
               play = 's';
           }
           repaint();
          }
    
        public void keyTyped(KeyEvent event) {}
        public void keyReleased(KeyEvent event) {}
    }
    
    // -------------------------------------------------------------------------------
    private class Connect4Panel extends JPanel {
      
      // Connect4Panel constructor
      public Connect4Panel() {
          blankTiles= new ArrayList<ArrayList<Ellipse2D.Double>> (7);
          ArrayList<Ellipse2D.Double> c1 = new ArrayList<Ellipse2D.Double> ();
          ArrayList<Ellipse2D.Double> c2 = new ArrayList<Ellipse2D.Double> ();
          ArrayList<Ellipse2D.Double> c3 = new ArrayList<Ellipse2D.Double> ();
          ArrayList<Ellipse2D.Double> c4 = new ArrayList<Ellipse2D.Double> ();
          ArrayList<Ellipse2D.Double> c5 = new ArrayList<Ellipse2D.Double> ();
          ArrayList<Ellipse2D.Double> c6 = new ArrayList<Ellipse2D.Double> ();
          
          // make tiles
          int x = 29;
          for (int i = 0; i < 7; i++) {
               c1.add(new Ellipse2D.Double(x,29,42,42));
               c2.add(new Ellipse2D.Double(x,79,42,42));
               c3.add(new Ellipse2D.Double(x,129,42,42));
               c4.add(new Ellipse2D.Double(x,179,42,42));
               c5.add(new Ellipse2D.Double(x,229,42,42));
               c6.add(new Ellipse2D.Double(x,279,42,42));
               x += 50; 
          }
          // adding all the tiles to the array list [] []
          blankTiles.add(c1); blankTiles.add(c2); blankTiles.add(c3); 
          blankTiles.add(c4); blankTiles.add(c5); blankTiles.add(c6); 
          
          // matrx used in background to check for win
          matrix = new char [] [] {{' ',' ',' ',' ',' ',' ',' '},
                                   {' ',' ',' ',' ',' ',' ',' '},
                                   {' ',' ',' ',' ',' ',' ',' '},
                                   {' ',' ',' ',' ',' ',' ',' '},
                                   {' ',' ',' ',' ',' ',' ',' '},
                                   {' ',' ',' ',' ',' ',' ',' '}};
          
          this.addKeyListener(new ListenerForKeys());
          this.setFocusable(true);
          repaint();
      }
    
     // -------------------------------------------------------------------------------
      public void paintComponent(Graphics g) {
          super.paintComponent(g);
          Graphics2D pen = (Graphics2D) g;
          // draw board 
          Rectangle2D.Double board = new Rectangle2D.Double(25, 25, 350, 300);
          pen.setColor(Color.BLUE);
          pen.fill(board);
          
          // draw tiles
          for (int i = 0; i < 6; i++) {
               for (int j = 0; j < 7; j++) {
                    symbol = matrix[i][j];
                    if (matrix[i][j] == 'R') {
                        pen.setColor(Color.RED);
                        pen.fill(blankTiles.get(i).get(j));
                        pen.draw(blankTiles.get(i).get(j));
                    } else if (matrix[i][j] == 'Y') {
                        pen.setColor(Color.YELLOW);
                        pen.fill(blankTiles.get(i).get(j));
                        pen.draw(blankTiles.get(i).get(j));
                    } else if (matrix[i][j] == ' ') {
                        pen.setColor(Color.WHITE);
                        pen.fill(blankTiles.get(i).get(j));
                        pen.draw(blankTiles.get(i).get(j));
                    }
               }
          }
          
          /*
          // for debugging purposes
          System.out.println("matrix");
          for (int i = 0; i < 6; i++) {
            System.out.println(Arrays.toString(matrix[i]));
          }
          */
         
      }     
    
    }
   
    // -------------------------------------------------------------------------------
    
      // Connect4 contructor 
      public Connect4() {

          this.setLayout(new BorderLayout());
          JPanel panel = new JPanel();
          panel.setBackground(new Color(173,221,230));
          this.add(panel, BorderLayout.NORTH);
                 
          Connect4Panel connectPanel = new Connect4Panel();
          this.add(connectPanel, BorderLayout.CENTER);
          connectPanel.setBackground(new Color(173,221,230));
          
          String intructions = "Try to connect 4 tiles in a row!";
          JLabel intructionsLabel = new JLabel(intructions);
          intructionsLabel.setFont(new Font("Arial", Font.PLAIN, 20));
          panel.setSize(500,500);
          panel.add(intructionsLabel);
            
          this.setSize(400, 400);
          this.setTitle("Connect Four");
          this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
          this.setVisible(true);
          
      }
      
      // main program
      public static void main(String[] args) { 
          Connect4 connect4 = new Connect4();
      }
}




