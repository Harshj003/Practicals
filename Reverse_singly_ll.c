#include <stdio.h>
#include <stdlib.h>
struct node {
 int data; //Data part
 struct node *next; //Address part
}*head;
void createList(int n);
void reverseList();
void displayList();
int main()
{
 int n, choice;
 printf("Enter the total number of nodes: ");
 scanf("%d", &n);
 createList(n);
 printf("\nData in the list \n");
 displayList();
 printf("\nPress 1 to reverse the order of singly linked list\n");
 scanf("%d", &choice);
 if(choice == 1)
 {
 reverseList();
 }
 printf("\nData in the list\n");
 displayList();
 return 0;
}
void createList(int n)
{
 struct node *newNode, *temp;
 int data, i;
 if(n <= 0)
 {
 printf("List size must be greater than zero.\n");
 return;
 }
 head = (struct node *)malloc(sizeof(struct node));
 
 if(head == NULL)
 {
 printf("Unable to allocate memory.");
 }
 else
 {
 printf("Enter the data of node 1: ");
 scanf("%d", &data);
 head->data = data; // Link the data field with data
 head->next = NULL; // Link the address field to NULL
 temp = head;
 for(i=2; i<=n; i++)
 {
 newNode = (struct node *)malloc(sizeof(struct node));
 if(newNode == NULL)
 {
 printf("Unable to allocate memory.");
 break;
 }
 else
 {
 printf("Enter the data of node %d: ", i);
 scanf("%d", &data);
 newNode->data = data; // Link the data field of newNode with data
 newNode->next = NULL; // Link the address field of newNode with NULL
 temp->next = newNode; // Link previous node i.e. temp to the newNode
 temp = temp->next;
 }
 }
 printf("SINGLY LINKED LIST CREATED SUCCESSFULLY\n");
 }
}
void reverseList()
{
 struct node *prevNode, *curNode;
 if(head != NULL)
 {
 prevNode = head;
 curNode = head->next;
 head = head->next;
 prevNode->next = NULL; // Make first node as last node
 while(head != NULL)
 {
 head = head->next;
 curNode->next = prevNode;
 prevNode = curNode;
 curNode = head;
 }
 head = prevNode; // Make last node as head
 printf("SUCCESSFULLY REVERSED LIST\n");
 }
}
void displayList()
{
 struct node *temp;
 if(head == NULL)
 {
 printf("List is empty.");
 }
 else
 {
 temp = head;
 while(temp != NULL)
 {
 printf("Data = %d\n", temp->data); // Print the data
of current node
 temp = temp->next; // Move to next node
 }
 }
 }
