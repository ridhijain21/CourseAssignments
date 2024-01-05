#include<stdlib.h>
# define MAXSIZE 5
struct fifo
{
    int arr[MAXSIZE];
    int front;
    int rear;
};
typedef struct fifo Queue;
Queue *createQueue(Queue *q)
{
    q -> front = -1;
    q -> rear = -1;
}
int isFullQueue(Queue *q)
{   
    if(q -> front == 0 && q -> rear == (MAXSIZE - 1)){
        return 1;
    }
    else if(q -> front  == q -> rear + 1){
        return 1;
    }
    else{
        return 0;
    }
}
int isEmptyQueue(Queue *q)
{
    if(q -> front == -1 || q -> rear == -1){
        return 1;
    }
    else{
        return 0;
    }
}
int singleelement(Queue *q)
{
    if(q -> rear == q -> front){
        printf("single element");
    }
    else{
        printf("Non single element");
    }
}
void ENQUEUE(Queue *q ,int key)
{
    if(isFullQueue(q)){
        printf("Queue Overflow\n");
    }
    else if(q -> front == -1 && q -> rear == -1){
        q -> front = q -> rear = 0;
        q -> arr[q -> rear] = key;
    }
    else if(q -> rear == MAXSIZE - 1 && q ->front != 0){
        q -> rear = 0;
        q -> arr[q -> rear] = key;
    }
    else{
        q -> rear++;
        q -> arr[q -> rear] = key;
    }
}
int DEQUEUE(Queue *q)
{
    if(isEmptyQueue(q)){
        printf("Queue Underflow");
    }
    else if(q -> front == MAXSIZE - 1){
        q -> front = 0;
    }
    else{
        q -> front++;
    }
}
void displayQueue(Queue *q)
{
    if (q -> rear >= q -> front){
        for(int i = q -> front; i <= q -> rear; i++)
            printf("%d ",q -> arr[i]);
    }
    else{
        for(int i = q -> front; i <= MAXSIZE-1; i++)
            printf("%d ", q -> arr[i]);
        for(int i =0 ; i <= q -> rear; i++)
            printf("%d ", q -> arr[i]);
    }
    printf("\n");
}
int countQueue(Queue *q)
{
   // count the number of elments in queue
    int count1 = 0,count2 = 0, count3 =0;
    if (q -> rear >= q -> front){
        for(int i = q -> front; i <= q -> rear; i++)
            count1++;
    }
    else{
        for(int i = q -> front; i < MAXSIZE; i++)
            count2++;
        for(int i = 0; i <= q -> rear; i++)
            count3++;
        count1 = count2+ count3;
    }
    printf("Number of elements:%d\n",count1);
}
int main()
{
    struct fifo q;
    createQueue(&q);
    ENQUEUE(&q,24);
    displayQueue(&q);
    ENQUEUE(&q,25);
    displayQueue(&q);
    ENQUEUE(&q,26);
    displayQueue(&q);
    ENQUEUE(&q,27);
    displayQueue(&q);
    ENQUEUE(&q,28);
    displayQueue(&q);
    ENQUEUE(&q,29);
    displayQueue(&q);
    DEQUEUE(&q);
    displayQueue(&q);
    ENQUEUE(&q,30);
    displayQueue(&q);
    ENQUEUE(&q,31);
    displayQueue(&q);
    countQueue(&q);
    singleelement(&q);
}

