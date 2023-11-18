import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
    static int[][] miro;
    static boolean[][] visited;
    static int[][] distacne;
    static int n,m;
    public static class Node{
        int x;
        int y;

        Node(int x, int y){
            this.x = x;
            this.y = y;
        }
    }

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st =  new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        miro = new int[n][m];
        visited = new boolean[n][m];
        distacne = new int[n][m];


        for(int i = 0; i < n ;i++){
            String s = br.readLine();

            for(int j = 0; j < m; j++){
                miro[i][j] = s.charAt(j) - '0';
            }
        }
        bfs(0,0);
        System.out.println(distacne[n-1][m-1]);
    }

    private static void bfs(int a, int b){

        Queue<Node> q = new LinkedList<>();
        q.add(new Node(a,b));
        visited[a][b] = true;
        distacne[a][b] = 1;

        int[] dx = {1,0,-1,0};
        int[] dy = {0,1,0,-1};
        while(!q.isEmpty()){
            Node node = q.poll();

            for(int i = 0; i < 4; i++){
                int nx = node.x + dx[i];
                int ny = node.y + dy[i];

                if(nx >= n || nx < 0 || ny >= m || ny < 0)
                    continue;
                if(visited[nx][ny] || miro[nx][ny] == 0)
                    continue;

                q.add(new Node(nx,ny));
                visited[nx][ny] = true;
                distacne[nx][ny] = distacne[node.x][node.y] + 1;
            }
        }
    }
}
