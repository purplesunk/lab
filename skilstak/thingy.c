#include <stdio.h>
#include <string.h>

// ponele
int letter(char *string, int lenght) {
    if (lenght == -1) return lenght;

    if (string[lenght] == '\0') {
        return lenght - 1;
    }

    int num = letter(string, lenght + 1);
    printf("%c", string[num]);
    return lenght - 1;
}

int otherthing(char *string, int lenght) {
    if (lenght == -1) return lenght;

    printf("%c", string[lenght]);

    return otherthing(string, lenght - 1);
}

int main() {
    int a =  letter("Hola mundo", 0);
    printf("\n");
    a = otherthing("Hola mundo", strlen("Hola mundo"));
    printf("\n");
    return a;
}

// I don't feel like they are good
