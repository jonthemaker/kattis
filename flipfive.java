import java.util.Scanner;

public class flipfive {
  public static Scanner scan = new Scanner(System.in);
  public static void main(String[] args) {
    int nBoxes = Integer.parseInt(scan.nextLine());
    Three[] three = new Three[nBoxes];
    int count = 0;
    String[] line = new String[3];
    for (int i = 0; i < nBoxes*3; i++) {
      line[i%3] = scan.nextLine();
      if (i%3 == 2) {
        three[count++] = new Three(line);
      }
    }
    for (int i = 0; i < three.length; i++) {
      three[i].display();
      System.out.println(three[i].project());
      three[i].display();
      System.out.println();
    }
  }
}
class Three {
  int[][] matrice;
  public Three(int[][] matrice) {
    this.matrice = new int[3][3];
    for (int r = 0; r < 3; r++) {
      for (int c = 0; c < 3; c++) {
        this.matrice[r][c] = matrice[r][c];
      }
    }
  }
  public Three(String[] list) {
    matrice = new int[3][3];
    for (int i = 0; i < list.length; i++) {
      for (int j = 0; j < 3; j++) {
        matrice[i][j] = ((int)(list[i].charAt(j)) - 42)/4;
      }
    }
  }
  public boolean project() {
    return project(clone(), 0, 5);
  }
  private boolean project(Three state, int depth, int inDepth) {
    // if (ready) {
    //   return true;
    // }
    if (depth < inDepth) {
      for (int r = 0; r < 3; r++) {
        for (int c = 0; c < 3; c++) {
          System.out.println("state:");
          state.display();
          Three a = state.clone();
          boolean ready = a.flipCross(r,c);
          System.out.println(ready+" <- "+depth);
          if (ready == false) {
            System.out.println("r:"+r+", c:"+c);
            System.out.println("a:");
            a.display();
          } else {
            return true;
          }
        }
      }
      for (int r = 0; r < 3; r++) {
        for (int c = 0; c < 3; c++) {
          Three b = state.clone();
          boolean ready = b.flipCross(r,c);
          if (ready == false) {
            ready = project(b, depth+1, inDepth);
            if (ready) {
              return true;
            }
          } else {
            return true;
          }
        }
      }
    }
    return false;
  }
  public boolean flipCross(int r, int c) {
    if (r >= 0 && r < matrice.length
    && c >= 0 && c < matrice[r].length) {
      flip(r, c);
      flip(r+1, c);
      flip(r-1, c);
      flip(r, c+1);
      flip(r, c-1);
    }
    for (int i = 0; i < 3; i++) {
      for (int j = 0; j < 3; j++) {
        if (matrice[i][j] == 0) {
          return false;
        }
      }
    }
    return true;
  }
  private void flip(int r, int c) {
    if (r >= 0 && r < matrice.length
    && c >= 0 && c < matrice[r].length) {
      matrice[r][c] = (matrice[r][c] + 1)%2;
    }
  }
  public Three clone() {
    return new Three(matrice);
  }
  public void display() {
    System.out.println("===");
    for (int r = 0; r < 3; r++) {
      for (int c = 0; c < 3; c++) {
        System.out.print(matrice[r][c]);
      }
      System.out.println();
    }
    System.out.println();
  }
}