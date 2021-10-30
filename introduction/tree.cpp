#include <bits/stdc++.h>
using namespace std;
struct TreeNode
{
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};
TreeNode *BuildTree()
{
    int d;
    cin >> d;
    if (d == -1)
        return NULL;
    TreeNode *Node = new TreeNode(d);
    cout << "Enter the left child of " << d << " : ";
    Node->left = BuildTree();
    cout << "Enter the right child of " << d << " : ";
    Node->right = BuildTree();
    return Node;
}
int get_height(TreeNode *root)
{
    if (root == NULL)
        return 0;
    int l = get_height(root->left);
    int r = get_height(root->right);
    return max(l, r) + 1;
}
bool treeHelper(TreeNode *root, int h, int l)
{
    if (root == NULL)
        return true;
    if (root->right == NULL && root->left == NULL)
    {
        if (h == l + 1)
            return true;
        else
            return false;
    }
    return treeHelper(root->left, h, l + 1) && treeHelper(root->right, h, l + 1);
}
bool check(TreeNode *root)
{
    int h = get_height(root);
    // cout<<h<<endl;
    int cur_l = 0;//current level, (root is always at level 0).
    return treeHelper(root, h, cur_l);
}
void print(TreeNode *root)
{
    if (root == NULL)
        return;
    cout << root->val << " ";
    print(root->left);
    print(root->right);
}
int main()
{
    cout << "Build first tree : ";
    TreeNode *root = BuildTree();
    cout << "PreOrder of Tree is: ";
    print(root);
    cout << "Are all Leaves at same level : " << boolalpha << check(root);
}
