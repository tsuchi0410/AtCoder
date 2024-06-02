"""
一番上に貼る

itertools I;
vl v = {1, 2, 3};
vvl comb = I.combinations(v, 2);

vvl perm = I.permutations(v);

vvl pro = I.product(v, 3);

"""


class itertools{
public:
    //----------------------------combinations---------------------------    
    vector<vector<long long>> combinations(vector<long long> lis,long long repeat){
        long long cnt=0;
        deque<set<long long>> d;
        set<long long> s,tmp;
        d.push_back(s);
        while (cnt<repeat){
            deque<set<long long>> d2;
            for(auto itr=d.begin(); itr!=d.end(); itr++){
                for(auto it=lis.begin()+cnt; it!=lis.begin()+lis.size()+cnt-repeat+1 ; it++){
                    tmp=*itr;
                    tmp.insert(*it);
                    if (tmp.size()==cnt+1){
                        d2.push_back(tmp);
                    }
                }
            }
            d=d2;
            cnt++;
        }
        sort(d.begin(), d.end());
        decltype(d)::iterator result = unique(d.begin(), d.end());
        d.erase(result, d.end());
        vector<vector<long long>> ans;
        for(auto item:d){
            vector<long long> ite(item.begin(),item.end());
            ans.push_back(ite);
        }
        return ans;
    }
    //----------------------------combinations---------------------------

    //----------------------------permutations---------------------------
    vector<vector<long long>> permutations(vector<long long> lis){
        vector<long long> range,tmp(lis.size(),0);
        vector<vector<long long>> ans;

        for(long long i=0  ;i<lis.size()  ;i++){
            range.push_back(i);
        }

        do{
            for(long long i=0  ;i<lis.size()  ;i++){
                tmp[range[i]]=lis[i];
            }
            ans.push_back(tmp);
        }while (next_permutation(range.begin(), range.end()));
        return ans;
    }
    //----------------------------permutations---------------------------

    //------------------------------product------------------------------
    vector<vector<long long>> ary;
    vector<long long> lis;
    vector<long long> tmp;

    void repeating (vector<long long> nums ,vector<long long> lis ,long long repeat){
        if (lis.size()==repeat){
            ary.push_back(lis);
        }else{
            tmp=lis;
            for (auto item:nums){
                tmp.push_back(item);
                repeating(nums,tmp,repeat);
                tmp=lis;
            }
        }
    }

    vector<vector<long long>> product(vector<long long> nums,long long repeat){
        repeating(nums,lis,repeat);
        return ary;
    //------------------------------product------------------------------
    };
};