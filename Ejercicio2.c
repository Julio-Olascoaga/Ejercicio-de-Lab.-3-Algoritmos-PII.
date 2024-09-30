#include <stdio.h>
#include <time.h>

unsigned long long fibonacci(int n) {
    if (n <= 1) {
        return n;
    }
    return fibonacci(n - 1) + fibonacci(n - 2);
}

int main() {
    int n;
    clock_t start, end;
    double cpu_time_used;

    printf("N= | Tiempo\n");
    printf("----|--------\n");
    
    for (n = 1; n <= 45; n++) { 
        start = clock();
        fibonacci(n);
        end = clock();
        
        cpu_time_used = ((double)(end - start)) / CLOCKS_PER_SEC * 1000; 
        printf("%d    | %.2f ms\n", n, cpu_time_used);
    }

    return 0;
}
