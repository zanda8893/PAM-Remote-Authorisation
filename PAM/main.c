#include <security/pam_modules.h>
#include <stdio.h>
#include <string.h>
#include <fcntl.h>
#include <sys/stat.h>
#include <sys/types.h>
#include <unistd.h>
#include <stdlib.h>



PAM_EXTERN int pam_sm_authenticate(pam_handle_t *pamh, int flags, int argc, const char **argv) {
    const char *user;
    char username[1024];

    FILE *write;
    FILE *read;

    pam_get_user(pamh, &user, "Username: ");

    //mkfifo("/tmp/py-c", 0666);

    write = fopen("/tmp/py-c", "w");

    fprintf(write, user);

    fclose(write);

    read = fopen("/tmp/py-c", "r");


    fgets(username,1023,read);

    fclose(read);

    return PAM_SUCCESS;

    //return PAM_AUTH_ERR;

}

PAM_EXTERN int pam_sm_setcred(pam_handle_t *pamh, int flags, int argc, const char **argv) {
    return PAM_SUCCESS;
}

int main() {
    FILE *read;
    read = fopen("/home/zanda/sudo-remote-approval/py-c", "r");

    char username[1024];


    fgets(username,1023,read);

    fclose(read);

    printf("Username: %s\n", username);

    FILE *write;
    write = fopen("/home/zanda/sudo-remote-approval/py-c", "w");

    fprintf(write, username);

    fclose(write);
}
