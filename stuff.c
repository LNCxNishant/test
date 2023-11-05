#include<stdio.h>

int main() {
int a[100];
int b[100];
int count = 0;
int temp = 0;
int n;

printf("enter the size of the data\n");
scanf("%d", &n);
printf("enter data\n");

for(int i = 0; i < n; i++) {
scanf("%d", &a[i]);
}

for(int i = 0; i < n; i++) {
if(a[i] == 1) {
count++;
b[temp] = a[i];
temp++;
}
else if(a[i] == 0) {
count = 0;
b[temp] = a[i];
temp++;
}
if(count > 4) {
count = 0;
b[temp] = 0;
temp++;
}
}

printf("data after stuffing\n");

for(int i = 0; i < temp; i++) {
printf("%d", b[i]);
}

int atemp = 0;
int c[100];
count = 0;

for(int i = 0; i < temp; i++) {
if(b[i] == 1) {
count++;
c[atemp] = b[i];
atemp++;
}
else if(b[i] == 0) {
count = 0;
c[atemp] = b[i];
atemp++;
}
if(count == 5) {
i++;
count = 0;
}
}

printf("\n data after stuffing is\n");
for(int i = 0; i < atemp; i++) {
printf("%d", c[i]);
}

return 0;
}
