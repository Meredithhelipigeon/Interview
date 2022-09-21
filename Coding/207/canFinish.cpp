class Solution {
public:
    bool canFinish(int numCourses, vector<vector<int>>& prerequisites) {
        bool visited[numCourses];
        memset(visited,false,sizeof(visited));
        
        std::unordered_map <int, vector<int>> prereq_to_class;
        std::unordered_map <int, std::unordered_set <int>> class_to_prereq;
        
        for(auto p: prerequisites){
            if (prereq_to_class.find(p[0])==prereq_to_class.end()){
                prereq_to_class[p[0]] = vector<int>(1,p[1]);
            } else {
                prereq_to_class[p[0]].emplace_back(p[1]);
            }
            if (class_to_prereq.find(p[1])==class_to_prereq.end()) {
                class_to_prereq[p[1]] = std::unordered_set <int> {p[0]};
            } else {
                class_to_prereq[p[1]].insert(p[0]);
            }
        }
        
        std::queue<int> my_queue;
        for(int i = 0; i < numCourses; ++i){
            // no prerequisties
            if (class_to_prereq.find(i)==class_to_prereq.end()){
                my_queue.emplace(i);
                visited[i] = true;
            }
        }
        
        while (my_queue.size()>0){
            int cur = my_queue.front();
            my_queue.pop();
            for(auto i: prereq_to_class[cur]) {
                if(!visited[i]) {
                    class_to_prereq[i].erase(cur);
                    if (size(class_to_prereq[i])==0){
                        my_queue.emplace(i);
                        visited[i] = true;
                    }
                }
            }
        }
        
        for(int i = 0; i < numCourses; ++i){
            if (!visited[i]) return false;
        }
        return true;
    }
};

class Solution2 {
public:
    
    bool isCycle(std::unordered_map<int, vector<int>> & prereq_to_classes, int cur, vector<bool> & check, vector<bool> & path) {
        if (check[cur]){
            return false;
        }
        if (path[cur]){
            return true;
        }
        path[cur]=true;
        
        bool ret = false;
        if (prereq_to_classes.find(cur)!=prereq_to_classes.end()){
            for(auto i: prereq_to_classes[cur]){
                ret = isCycle(prereq_to_classes, i, check, path);
                if (ret) {
                    return true;
                }
            }
        }
        
        check[cur]=true;
        path[cur]=false;
        return ret;
    }
    
    bool canFinish(int numCourses, vector<vector<int>>& prerequisites) {
        std::unordered_map<int, vector<int>> prereq_to_classess;
        for(auto p: prerequisites){
            if (prereq_to_classess.find(p[1])!=prereq_to_classess.end()){
                prereq_to_classess[p[1]].emplace_back(p[0]);
            } else {
                prereq_to_classess[p[1]] = vector<int>{p[0]};
            }
        }
        
        vector<bool> check(numCourses, false);
        vector<bool> path(numCourses, false);
        for(int i = 0; i < numCourses; ++i){
            if (check[i]!=true){
                if (isCycle(prereq_to_classess, i, check, path)){
                    return false;
                }
            }
        }
        return true;
    }
};
