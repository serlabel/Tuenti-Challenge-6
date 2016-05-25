#include <iostream>
#include <vector>

using namespace std;

int N, M;
int m[1000][1000];
int matrix2[2000][2000];
int kadane[2000];

int get_kadane()
{
  int max_local = 0, max_global = 0;
  for(int i=0; i<2*M; i++)
  {
    max_local = max(0, max_local + kadane[i]);
    max_global = max(max_local, max_global);
  }
  return max_global;
}

int tiles()
{
  // Duplicate the matrix
  for(int i=0; i<N; i++)
  {
    for(int j=0; j<M; j++)
    {
      matrix2[i][j] = m[i][j];
      matrix2[i][j+M] = m[i][j];
      matrix2[i+N][j] = m[i][j];
      matrix2[i+N][j+M] = m[i][j];
    }
  }

  // Get the vertical prefix sum
  for(int i=2*N-1; i>=0; i--)
  {
    for(int j=0; j<2*M; j++)
    {
      for(int k=i+1; k<2*N; k++)
	matrix2[k][j] += matrix2[i][j];
    }
  }

  int best_sum = 0;
  for(int a=0; a<2*N; a++)
  {
    for(int b=a; b<2*N; b++)
    {
      for(int col=0; col<2*M; col++)
      {
	kadane[col] = matrix2[b][col];
	if(a != 0)
	  kadane[col] -= matrix2[a-1][col];
      }
      int sum = get_kadane();
      if(best_sum < sum)
	best_sum = sum;
    }
  }
  
  return best_sum;
}

bool inf_matrix()
{
  int total_sum = 0;
  vector<int> rows_sum(N, 0);
  vector<int> cols_sum(M, 0);
  for(int i=0; i<N; i++)
  {
    for(int j=0; j<M; j++)
    {
      total_sum += m[i][j];
      rows_sum[i] += m[i][j];
      cols_sum[j] += m[i][j];
    }
  }

  if(total_sum > 0)
    return true;
  for(int i=0; i<N; i++)
  {
    if(rows_sum[i] > 0)
      return true;
  }
  for(int i=0; i<M; i++)
  {
    if(cols_sum[i] > 0)
      return true;
  }
  return false;
}

int main()
{
  int test_cases;
  string row;
  cin >> test_cases;
  for(int c=1; c<=test_cases; c++)
  {
    cin >> N >> M;
    for(int i=0; i<N; i++)
    {
      cin >> row;
      for(int j=0; j<M; j++)
      {
	if(row[j] >= 'a' && row[j] <= 'z')
	  m[i][j] = -(row[j] - 'a' + 1);
	else if(row[j] >= 'A' && row[j] <= 'Z')
	  m[i][j] = row[j] - 'A' + 1;
	else
	  m[i][j] = 0;
      }
    }

    // If matrix or one column/row sums more than 0 -> INFINITY
    if(inf_matrix())
      cout << "Case #" << c << ": INFINITY" << endl;
    else
      cout << "Case #" << c << ": " << tiles() << endl;
  }
  return 0;
}
