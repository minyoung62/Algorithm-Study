
import java.util.*;

class Pos {
  int end;
  int weight;

  Pos(int end, int weight) {
    this.end = end;
    this.weight = weight;
  }
}

public class Main {

  static int n, m, s, e;
  static ArrayList<List<Pos>> graph = new ArrayList<>();
  static ArrayList<Pos> posPoll = new ArrayList<>();
  static int[] visited = new int[10001];
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    n = sc.nextInt();
    m = sc.nextInt();
    int u, v, weight;
    for (int i = 0; i < n + 1; i++) {
      graph.add(new ArrayList<>());
    }

    for(int i = 0; i < 10001; i++) {
      posPoll.add(new Pos(0,0));
    }

    for (int i = 0; i < m; i++) {
      u = sc.nextInt();
      v = sc.nextInt();
      weight = sc.nextInt();
      graph.get(u).add(new Pos(v, weight));
      graph.get(v).add(new Pos(u, weight));
    }
    s = sc.nextInt();
    e = sc.nextInt();
    boolean[] visited = new boolean[n + 1];


    int l = 1, r = 1000000000;
    int mid, ans = 0;
    while (l <= r) {
      mid = (l + r) / 2;
      if (isPossible(mid, visited)) {
        ans = mid;
        l = mid + 1;

      } else {
        r = mid - 1;
      }
    }
    System.out.println(ans);
  }

  private static boolean isPossible(int limitWeight, boolean[] visited) {
    Deque<Pos> q = new ArrayDeque<>();
    Arrays.fill(visited, false);

    q.add(new Pos(s, 0));
    visited[s] = true;
    int x, weight;

    while (q.size()!=0) {
      Pos pos = q.poll();
      x = pos.end;
      weight = pos.weight;

      if (x == e) return true;

      for (int i = 0; i < graph.get(x).size(); i++) {
        Pos nextPos = graph.get(x).get(i);

        if (!visited[nextPos.end] && limitWeight <= nextPos.weight) {
          visited[nextPos.end] = true;
          posPoll.get(nextPos.end).end = nextPos.end;
          posPoll.get(nextPos.end).weight = nextPos.weight;

          q.add(posPoll.get(nextPos.end));
        }
      }

    }
    return false;
  }
}
