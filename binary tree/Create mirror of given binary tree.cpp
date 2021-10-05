//Bhaskar Varshney
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
void print(TreeNode *root)
{
    if (root == NULL)
        return;
    print(root->left);
    cout << root->val << " ";
    print(root->right);
}
void mirror(TreeNode *root)
{
    if (root == NULL)
        return;
    TreeNode *temp = root->left;
    root->left = root->right;
    root->right = temp;
    mirror(root->left);
    mirror(root->right);
}
// or
// TreeNode *invertTree(TreeNode *root)
// {
//     if (root == NULL)
//         return NULL;
//     TreeNode *temp = root->right;
//     // we have to keep the value of root->right or root->left befor entering into traversals,
//     // bcz while returning the node in left traversal the returned value will be stored in opposite side.
//     // i.e, if we entered first in left subtree than the left subtree root will be returned and stored in (root->right) right pointer ofparent node.
//     // and hence, we've lost the address of right subtree, therefore for entering in right subtree we've used that value we've stored initially in temp.
//     // and now the address of right subtree root node will be returned and stored in (root->left) left pointer of parent node;
//     root->right = invertTree(root->left);
//     root->left = invertTree(temp);
//     return root;
// }
int main()
{
    TreeNode *root = BuildTree();
    cout << "Inorder of Tree is: ";
    print(root);
    cout << endl;
    mirror(root);
    // root = invertTree(root);
    cout << "Inorder of Mirror Tree is: ";
    print(root);
}
