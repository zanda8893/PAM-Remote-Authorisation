#include <security/pam_modules.h>
#include <stdio.h>
#include <string.h>
#include <fcntl.h>
#include <sys/stat.h>
#include <sys/types.h>
#include <unistd.h>
#include <stdlib.h>


int handle_sudo(char *cmd, char *user){
    FILE *write;
    FILE *read;

    char response[1024];
    char *user_cmd;

    strcpy(user_cmd,user);
    strcat(user_cmd," ");
    strcat(user_cmd, cmd + 5);

    write = fopen("/tmp/py-c", "w");

    fprintf(write, user_cmd);

    fclose(write);
    read = fopen("/tmp/py-c", "r");


    fgets(response,1023,read);


    fclose(read);

    strcat(user_cmd," ");
    strcat(user_cmd,"1");


    if (strcmp(response, user)) {
        return 0;
    }
    return 1;
}

PAM_EXTERN int pam_sm_authenticate(pam_handle_t *pamh, int flags, int argc, const char **argv) {
    const char *user;
    char proc[1024];
    char *cmd; // Max file name length plus \0
    int return_val = 1;

    FILE *fcmdline;
    char cmdline[1024];

    pam_get_user(pamh, &user, "Username: ");

    pid_t pid = getpid();

    snprintf(proc,sizeof(proc), "/proc/%d/cmdline", pid);


    fcmdline = fopen(proc, "r");
    fgets(cmdline,1023,fcmdline);
    fclose(fcmdline);


    cmd = strtok(cmdline," ");

    mkfifo("/tmp/py-c", 0666);

    if (strcmp(cmd, "sudo") == 0) {
        return_val = handle_sudo(cmd, user);
    }

    if (return_val == 0) {
        return PAM_SUCCESS;
    }


    return PAM_AUTH_ERR;

}

PAM_EXTERN int pam_sm_setcred(pam_handle_t *pamh, int flags, int argc, const char **argv) {
    return PAM_SUCCESS;
}

