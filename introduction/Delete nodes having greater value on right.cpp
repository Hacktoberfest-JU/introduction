#include <iostream>
using namespace std;
struct ListNode
{
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};
ListNode *BuildList()
{
    ListNode *head = NULL, *temp;
    int choice = 1;
    while (choice == 1)
    {
        ListNode *newnode = (ListNode *)malloc(sizeof(ListNode));
        cout << "Enter data : ";
        cin >> newnode->val;
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
void print(ListNode *head)
{
    ListNode *temp = head;
    while (temp != NULL)
    {
        cout << temp->val << " ";
        temp = temp->next;
    }
}
ListNode *rev(ListNode *head)
{
    if (head == NULL || head->next == NULL)
        return head;
    ListNode *cur, *nxt = head, *prev = NULL;
    while (nxt != NULL)
    {
        cur = nxt;
        nxt = nxt->next;
        cur->next = prev;
        prev = cur;
    }
    return prev;
}
ListNode *compute(ListNode *head)
{
    head = rev(head);
    ListNode *temp = head, *pre;
    int mx = -1;
    while (temp != NULL)
    {
        if (temp->val >= mx)
        {
            mx = temp->val;
            pre = temp;
            temp = temp->next;
        }
        else
        {
            pre->next = temp->next;
            free(temp);
            temp = pre->next;
        }
    }
    head = rev(head);
    return head;
}

// OR

// ListNode *compute(ListNode *head)
// {
//     if (head == NULL || head->next == NULL)
//         return head;
//     head = rev(head);
//     ListNode *temp = head;
//     while (temp != NULL)
//     {
//         if (temp->next != NULL && temp->data > temp->next->data)
//         {
//             temp->next = temp->next->next;
//             temp = temp->next;
//         }
//         else
//             temp = temp->next;
//     }
//     head = rev(head);
//     return head;
// }

int main()
{
    cout << "Build list : \n";
    ListNode *head = BuildList();
    cout << "Original List : ";
    print(head);
    head = compute(head);
    cout << "\nList after deleting nodes having greater value on right ";
    print(head);
}
