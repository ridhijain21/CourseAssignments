#include<stdio.h>
#include<stdlib.h>
struct node                                  
{
    int data;                      
    struct node* link;                   //node definition
};
// code for insertion at end of the linked list
void insertatend(struct node **head,int x)
{   
    struct node *newnode = (struct node *)malloc(sizeof(struct node));
    newnode -> data = x;
    newnode -> link = NULL;
    if(*head == NULL){
        *head = newnode;
    }
    else{
        struct node *temp = *head;
        struct node *temp1;
        while(temp != NULL){
            temp1 = temp;
            temp = temp -> link;
        }
        temp1 -> link = newnode;
    }
}
// deletion of head node of the linked list
void deletionathead(struct node **head)
{
    if(*head == NULL){   // codition of checking an empty linked list
        printf("underflow");
    }
    else{
        struct node *temp = *head;
        *head = temp -> link;
        free(temp);
    }
}
// deletion of end node of linked list
void deletionatend(struct node **head)
{
    struct node *temp = *head;
    struct node *temp1;
    while(temp -> link != NULL){
        temp1 = temp;
        temp = temp -> link;
    }
    temp1 -> link = NULL;
    free(temp);
}
// deletion of any specific position in an linked list given by user
void deletionatpos(struct node **head,int pos)
{   
    struct node *temp = *head;
    for( int i = 2; i < pos ;i++){
        temp = temp -> link;
    }
    struct node *temp2 = temp -> link;
    temp -> link = temp -> link -> link;
    free(temp2);
}
// function for displaying updated linked list
void display(struct node *head)
{
    struct node* temp = head;
    while(temp != NULL){
        printf("%d ",temp -> data);
        temp = temp -> link;
    }
    printf("\n");
}
// declaration of main function
int main()
{   
    struct node *head = NULL;
    insertatend(&head,24);            
    insertatend(&head,25);
    insertatend(&head,26);
    insertatend(&head,28);
    insertatend(&head,29);
    insertatend(&head,30);
    insertatend(&head,31);            // insertion() function calling
    display(head);
    deletionathead(&head);           // deletionathead() function calling
    display(head);
    deletionatend(&head);            // deletionatend() function calling
    display(head);
    deletionatpos(&head,3);          // deltionatpos() fucntion calling
    display(head);
}


