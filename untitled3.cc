    #include <cstdio> 
    class UnsealTheSafe{ 
    public: 
      long long countPasswords(int N){ 
        long long d[50][20]; 
        int i; 
        for(i=0; i<=9; i++){ 
          d[1][i]=1; 
        } 
        for(i=2; i<=N; i++){ 
          d[i][0]=d[i-1][7]; 
          d[i][1]=d[i-1][2]+d[i-1][4]; 
          d[i][2]=d[i-1][1]+d[i-1][3]+d[i-1][5]; 
          d[i][3]=d[i-1][2]+d[i-1][6]; 
          d[i][4]=d[i-1][1]+d[i-1][5]+d[i-1][7]; 
          d[i][5]=d[i-1][2]+d[i-1][4]+d[i-1][6]+d[i-1][8]; 
          d[i][6]=d[i-1][3]+d[i-1][5]+d[i-1][9]; 
          d[i][7]=d[i-1][4]+d[i-1][8]+d[i-1][0]; 
          d[i][8]=d[i-1][5]+d[i-1][7]+d[i-1][9]; 
          d[i][9]=d[i-1][6]+d[i-1][8]; 
          d[i][0]=d[i-1][7]; 
        } 
        long long ans=0; 
        for(i=0; i<=9; i++){ 
          ans+=d[N][i]; 
        } 
        return ans; 
      } 
    };