#include <iostream>
using namespace std;
struct ListNode
{
    int data;
    ListNode *next;
    ListNode(int x) : data(x), next(nullptr) {}
};
ListNode *BuildList()
{
    ListNode *head = NULL, *temp;
    int choice = 1;
    while (choice == 1)
    {
        ListNode *newnode = (ListNode *)malloc(sizeof(ListNode));
        cout << "Enter data : ";
        cin >> newnode->data;
        newnode->next = 0;
        if (head == 0)
            head = temp = newnode;
        else
        {
            temp->next = newnode;
            temp = newnode;
        }
        cout << "Want another node to be inserted : ";
        cin >> choice;
    }
    return head;
}
bool is_Palindrome(ListNode *head, ListNode *&left)
{
    if (head == NULL)
        return true;
    bool result = is_Palindrome(head->next, left);
    if (result == false || (head->data != left->data))
    {
        return false;
    }
    //if previous result is not false and current (left and right) pointer's values are same than move left ahead and return true;
    left = left->next;
    return true;
}
int main()
{
    cout << "Build list : \n";
    ListNode *head = BuildList();
    ListNode *left = head;
    cout << "Is the list Palindrome : " << boolalpha << is_Palindrome(head, left);
}
