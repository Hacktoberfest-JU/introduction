#include <iostream>
#include <vector>
using namespace std;
struct DblyListNode
{
    int val;
    DblyListNode *next;
    DblyListNode *prev;
    DblyListNode()
    {
        val = 0;
        next = nullptr;
        prev = nullptr;
    }
    DblyListNode(int x)
    {
        val = x;
        next = nullptr;
        prev = nullptr;
    }
};
vector<DblyListNode *> BuildList()
{
    DblyListNode *head = NULL, *tail;
    int choice = 1;
    while (choice == 1)
    {
        DblyListNode *newnode = new DblyListNode();
        cout << "Enter data : ";
        cin >> newnode->val;
        if (head == 0)
            head = tail = newnode;
        else
        {
            tail->next = newnode;
            newnode->prev = tail;
            tail = newnode;
        }
        cout << "Want another node to be inserted : ";
        cin >> choice;
    }
    return {head, tail};
}
void print(DblyListNode *head)
{
    DblyListNode *temp = head;
    while (temp != NULL)
    {
        cout << temp->val << " ";
        temp = temp->next;
    }
}
void rev_print(DblyListNode *tail)
{
    DblyListNode *temp = tail;
    while (temp != NULL)
    {
        cout << temp->val << " ";
        temp = temp->prev;
    }
}
int main()
{
    cout << "Build list : \n";
    vector<DblyListNode *> v = BuildList();
    DblyListNode *head = v[0], *tail = v[1];
    cout << "Originl list is : ";
    print(head);
    cout << "Originl list in reverse order : ";
    rev_print(tail);
}
