import java.io.*;
import java.util.*;

class Pos {
  int x;
  int y;
  int crashed;

  Pos(int x, int y, int crashed) {
    this.x = x;
    this.y = y;
    this.crashed = crashed;
  }
}

class Main {
  static int wallCrashedMaxCnt = 2;

  static int n, m;
  static final int N = 1001;
  static int[][] a = new int[N][N];

  public static void main(String[] args) throws Exception {
    BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer st = new StringTokenizer(bf.readLine());

    n = Integer.parseInt(st.nextToken());
    m = Integer.parseInt(st.nextToken());

    for (int i = 0; i < n; i++) {
      String[] split = bf.readLine().split("");
      for (int j = 0; j < m; j++) {
        a[i][j] = Integer.parseInt(split[j]);
      }
    }
    int ans = bfs();
    System.out.println(ans);


  }

  private static boolean inRnage(int x, int y) {
    return 0 <= x && x < n && 0 <= y && y < m;
  }

  private static int bfs() {
    int[][][] visited = new int[n][m][wallCrashedMaxCnt];


    Queue<Pos> q = new LinkedList<>();
    q.add(new Pos(0, 0, 0));
    int x, y, nx, ny, crashed;
    int maxNum = 0;
    int[] dxs = {1, -1, 0, 0};
    int[] dys = {0, 0, 1, -1};
    while (!q.isEmpty()) {
      Pos pos = q.poll();
      x = pos.x;
      y = pos.y;
      crashed = pos.crashed;

      if (x == n - 1 && y == m - 1) {
        for (int i = 0; i < wallCrashedMaxCnt; i++) {
          maxNum = Math.max(maxNum, visited[n-1][m-1][i]);
        }
        return maxNum + 1;
      }

      for (int i = 0; i < 4; i++) {
        nx = x + dxs[i];
        ny = y + dys[i];

        if (!inRnage(nx, ny)) continue;

        // 벽이 아니고, 처음 방문 했을 때
        if (a[nx][ny] == 0 && visited[nx][ny][crashed] == 0) {
          visited[nx][ny][crashed] = visited[x][y][crashed] + 1;
          q.add(new Pos(nx, ny, crashed));
        }
        // 벽이고, 지금 현재 뿌순 벽 갯수가 최대 벽을 부술 수 있는 개수보다 작고, 처음 방문했을 때
        else if (a[nx][ny] == 1 && crashed + 1 < wallCrashedMaxCnt && visited[nx][ny][crashed] == 0) {
          visited[nx][ny][crashed + 1] = visited[x][y][crashed] + 1;
          q.add(new Pos(nx, ny, crashed + 1));
        }
      }


    }
    return -1;


  }
}
