import java.util.ArrayList;
import java.util.Scanner;
public class allpairspath {
  public static void main(String[] args) throws Exception {
    Scanner scan = new Scanner(System.in);
    int temp = -1;
    while (true) {
      temp++;
      String[] line = scan.nextLine().split(" ");
      if (line[0].equals("0") && line[1].equals("0") && line[2].equals("0")) {
         break;
      }
      if (temp > 0)
        System.out.println();
      Graph graph = new Graph(Integer.parseInt(line[0]));
      for (int j = 0; j < Integer.parseInt(line[1]); j++) {
        graph.connectEdge(scan.nextLine().split(" "));
      }
      for (int j = 0; j < Integer.parseInt(line[2]); j++) {
        System.out.println(graph.traverseFrom(scan.nextLine().split(" ")));
      }
    }
    scan.close();
  }
}
class Graph {
  Node[] nodes;
  public Graph(int size) {
    this.nodes = new Node[size];
    for (int i = 0; i < size; i++)
      this.nodes[i] = new Node(i);
  }
  public String traverseFrom(String[] args) {
    return traverseFrom(Integer.parseInt(args[0]), Integer.parseInt(args[1]));
  }
  public String traverseFrom(int a0, int a1) {
    String str = nodes[a0].traverse(nodes[a1]);
    for (int i = 0; i < nodes.length; i++) {
      nodes[i].nVisits = -1;
    }
    return str;
  }
  public void connectEdge(String[] args) {
    connectEdge(Integer.parseInt(args[0]), Integer.parseInt(args[1]), Integer.parseInt(args[2]));
  }
  public void connectEdge(int a0, int a1, int distance) {
    if (nodes[a0].next.size() == 0) {
      nodes[a0].next.add(new Edge(nodes[a1], distance));
      return;
    }
    for (int i = 0; i < nodes[a0].next.size(); i++) {
      if (distance < nodes[a0].next.get(i).v) {
        nodes[a0].next.add(i, new Edge(nodes[a1], distance));
      } else {
        nodes[a0].next.add(new Edge(nodes[a1], distance));
      }
      break;
    }
  }
}
class Edge {
  Node n;
  int v;
  public Edge(Node node, int value) {
    this.n = node;
    this.v = value;
  }
}
class Node {
  int ID;
  int nVisits;
  int min;
  ArrayList<Edge> next;
  public Node(int ID) {
    this.ID = ID;
    nVisits = -1;
    min = -2;
    next = new ArrayList<Edge>();
  }
  public String traverse(Node desired) {
    min = -1;
    if (this == desired) {
      return "0";
    }
    return traverse(this, desired, 0, "impossible");
  }
  public String traverse(Node ref, Node desired, int distTraveled, String txt) {
    if (this == desired) {
      if (ref.min == -1 || distTraveled < ref.min) {
        ref.min = distTraveled;
      }
      txt = "done";
    }
    while (nVisits < next.size()-1) {
      nVisits++;
      if (!txt.equals("done")) {
        // distTraveled += next.get(nVisits).v;//#
        txt = next.get(nVisits).n.traverse(ref, desired, distTraveled + next.get(nVisits).v/*!*/, txt);
      }
    }
    if (txt.equals("done")) {
      return ""+ref.min;
    } else {
      return txt;
    }
  }
}
