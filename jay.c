//variable,datatypes+input/output


//output


/*#include<stdio.h>
int main(){
    int age = 22;
    float pi = 3.14;
    char percentage = '%';
    printf("age is %d\n",age);
    printf("float is %f\n",pi);
    printf("percentage is %c\n",percentage);
    return 0;
}*/


//input sum of 2 number


/*#include<stdio.h>
int main()
{
    int a,b;
    printf("enter a\n");
    scanf("%d",&a);
    printf("enter b\n");
    scanf("%d",&b);
    printf("sum of a and b is : %d \n",a+b);
    return 0;
}*/


// area of a square


/*#include<stdio.h>
int main()
{
    float side;
    printf("enter side:");
    scanf("%f",&side);
    printf("area is:%f",side*side);
    return 0;
}*/


//area of circle


/*#include<stdio.h>
int main(){
float radius;
printf("enter radius:");
scanf("%f",&radius);
printf("area is : %f",3.14*radius*radius);
return 0;
}*/


//if else

#include<stdio.h>
int main()
{
    int age = 19;
    if(age >= 18){
    printf("you are eligible to vote");
    }
    else{
        printf("you are not eligible to vote:");
    }
    return 0;
}