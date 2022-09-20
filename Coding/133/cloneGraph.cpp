/*
// Definition for a Node.
class Node {
public:
    int val;
    vector<Node*> neighbors;
    Node() {
        val = 0;
        neighbors = vector<Node*>();
    }
    Node(int _val) {
        val = _val;
        neighbors = vector<Node*>();
    }
    Node(int _val, vector<Node*> _neighbors) {
        val = _val;
        neighbors = _neighbors;
    }
};
*/

class Solution {
public:
    std::unordered_map<int, Node*> visited_nodes;
    
    void dfs(Node* oldNode, Node * newNode){
        for (auto neighbor: oldNode->neighbors) {
            if (visited_nodes.find(neighbor->val) == visited_nodes.end()){
                Node * newNeighbor = new Node(neighbor->val);
                visited_nodes[neighbor->val] = newNeighbor;
                newNode->neighbors.emplace_back(newNeighbor);
                dfs(neighbor, newNeighbor);
            } else {
                newNode->neighbors.emplace_back(visited_nodes[neighbor->val]); 
            }
        }
    }
    
    Node* cloneGraph(Node* node) {
        if (node==NULL) return node;
        Node * newRoot = new Node(node->val);
        visited_nodes[node->val] = newRoot;
        dfs(node, newRoot);
        
        return newRoot;
    }
};
