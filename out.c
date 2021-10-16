#include <stdio.h>
int main(void){
float a;
float b;
float s;
float c;
a = 0;
while(a<1){
printf("Enter number of scores: \n");
if(0 == scanf("%f", &a)) {
a = 0;
scanf("%*s");
}
if(a==3){
printf("You chose 3\n");
}
else if(a==4){
printf("You chose 4\n");
}
else{
printf("You chose a different number\n");
}
}
b = 0;
s = 0;
printf("Enter one value at a time: \n");
while(b<a){
if(0 == scanf("%f", &c)) {
c = 0;
scanf("%*s");
}
s = s+c;
b = b+1;
}
printf("Average: \n");
printf("%.2f\n", (float)(s/a));
return 0;
}
