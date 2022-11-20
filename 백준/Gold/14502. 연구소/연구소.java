import java.io.*;
import java.util.*;

class Pos {
  int x;
  int y;

  Pos(int x, int y) {
    this.x = x;
    this.y = y;
  }
}

class Main {
  static int n, m, ans = 0;
  static int[][] map = new int[8][8];
  static boolean[][] visited = new boolean[8][8];

  static Pos[] wall = new Pos[3];
  static List<Pos> emptys = new ArrayList<>();
  static List<Pos> birus = new ArrayList<>();
  static int[] used = new int[8 * 8];

  public static void main(String[] args) throws Exception {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer st = new StringTokenizer(br.readLine());

    n = Integer.parseInt(st.nextToken());
    m = Integer.parseInt(st.nextToken());

    for(int i = 0; i < 3; i++) {
      wall[i] = new Pos(0,0);
    }

    for (int i = 0; i < n; i++) {
      st = new StringTokenizer(br.readLine());
      for (int j = 0; j < m; j++) {
        map[i][j] = Integer.parseInt(st.nextToken());
      }
    }

    for (int i = 0; i < n; i++) {
      for (int j = 0; j < m; j++) {
        if (map[i][j] == 0) {
          emptys.add(new Pos(i, j));
        } else if (map[i][j] == 2) {
          birus.add(new Pos(i, j));
        }
      }
    }

    choose(0);

    System.out.println(ans);
  }

  private static void choose(int cnt) {
    if (cnt == 3) {
      ans = Math.max(isPossible(), ans);
      return;
    }

    for (int i = 0; i < emptys.size(); i++) {
      if (used[i] == 1) continue;

      used[i] = 1;
      wall[cnt].x = emptys.get(i).x;
      wall[cnt].y = emptys.get(i).y;
      choose(cnt + 1);
      used[i] = 0;
    }

  }

  private static int isPossible() {
    int cnt = 0;
    for (int i = 0; i < wall.length; i++) {
      map[wall[i].x][wall[i].y] = 1;
    }

    for(int i = 0; i < n ; i++) {
      for(int j = 0; j <m; j++) {
        visited[i][j] = false;
      }
    }

    for (int i = 0; i < birus.size(); i++) {
      bfs(birus.get(i).x, birus.get(i).y);
    }

    for(int i = 0; i< n; i++) {
      for(int j = 0; j <m; j++) {
        if(!visited[i][j] && map[i][j] == 0) {
          cnt++;
        }
      }
    }

    for (int i = 0; i < wall.length; i++) {
      map[wall[i].x][wall[i].y] = 0;
    }
    return cnt;
  }

  private static void bfs(int i, int j) {
    Queue<Pos> q = new LinkedList<>();
    q.add(new Pos(i, j));
    visited[i][j] = true;
    int x, y, nx, ny;
    Pos pos;
    int[] dxs = {1, -1, 0, 0};
    int[] dys = {0, 0, 1, -1};
    while(!q.isEmpty()) {
      pos = q.poll();
      x = pos.x;
      y = pos.y;

      for(int k = 0; k < 4; k++) {
        nx = x + dxs[k];
        ny = y + dys[k];

        if(!inRnage(nx, ny) || visited[nx][ny]) continue;
        if(map[nx][ny] == 0) {
          visited[nx][ny] = true;
          q.add(new Pos(nx, ny));
        }


    }

  }
}

  private static boolean inRnage(int nx, int ny) {
    return 0 <= nx && nx < n && 0 <= ny && ny < m;
  }
  }

