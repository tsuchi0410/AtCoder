#include <bits/stdc++.h>
using namespace std;
int main(){
    int Q;
    cin >> Q;
    deque<int> dq;
    priority_queue<int, vector<int>, greater<int>> pq;
    
    for(int i = 0; i < Q; i++){
        int query;
        cin >> query;

        if(query == 1){
            int x;
            cin >> x;
            dq.push_back(x);

        }
        
        if(query == 2){
            if(pq.empty()){
                cout << dq.front() << endl;
                dq.pop_front();
            }else{
                cout << pq.top()<< endl;
                pq.pop();
            }
        }

        if(query == 3){
            while(!dq.empty()){
                int x = dq.front();
                dq.pop_front();
                pq.push(x);
            }
        }
    }
}