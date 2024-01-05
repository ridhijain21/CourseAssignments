#include<stdio.h>
#include<stdlib.h>                            
struct node
{
    int data;
    struct node *link;
};
// push function created to push elements 
void push(struct node **head,int data)             
{   
    struct node *newnode = (struct node *)malloc(sizeof(struct node));
    newnode -> data = data;
    newnode -> link = NULL; 
    if(*head == NULL){         
        *head = newnode;           
    }
    else{
        newnode -> link = *head;    
        *head = newnode;          
    }
}
// pop function created to pop the elements from stack in first out.
void pop(struct node **head)
{   
    struct node *temp = *head;
	if(*head == NULL){             
		printf("Underflow");
	} 
	else{
		*head = temp -> link;    
	} 
}
// is empty function check wheather the stack is empty or not.
void isempty(struct node *head)
{
	if(head == NULL){          
		printf("True\n"); 
	}
	else{
		printf("False\n");
	}
}
//display function display the data persent in stack
void display(struct node *head)
{
    struct node *temp = head;
    while(temp != NULL){                      
        printf("%d ", temp -> data);
        temp = temp -> link;
    }
	printf("\n");
}
int main()           
{
struct node *head = NULL; 
push(&head,24); 
push(&head,25);
push(&head,26);          
push(&head,27);
display(head);
pop(&head);              
pop(&head);
display(head);
isempty(head);        
pop(&head);
display(head);
isempty(head);
display(head);
pop(&head);
isempty(head);
}


