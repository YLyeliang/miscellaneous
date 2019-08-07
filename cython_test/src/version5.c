#include <math.h>
#include <stdio.h>
#include <time.h>
#define NUM 500000

//version5.c

float great_circle(float lon1,float lat1,float lon2,float lat2){
    float radius=3956.0;
    float pi=3.14159265;
    float x=pi/180.0;
    float a,b,theta,c;

    a=(90.0-lat1)*(x);
    b=(90.0-lat2)*(x);
    theta=(lon2-lon1)*(x);
    c=acos((cos(a)*cos(b))+(sin(a)*sin(b)*cos(theta)));
    return radius*c;
}

int main(){
    int i;
    float x;
    clock_t start, finish;
    double Total_time;
    start = clock();
    for(i=0;i<=NUM;i++)
        x=great_circle(-72.345,34.323,-61.823,54.826);
    finish = clock();
    Total_time = (double)(finish-start) / CLOCKS_PER_SEC;
    printf("%f sec",Total_time);
    printf("\n");
    printf("%f",x);
}