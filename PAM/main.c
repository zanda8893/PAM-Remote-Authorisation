#include <security/pam_modules.h>
#include <stdio.h>
#include <string.h>
#include <fcntl.h>
#include <sys/stat.h>
#include <sys/types.h>
#include <unistd.h>
#include <stdlib.h>
#include <signal.h>

int stop = 0;

void sigint_handler(int signum) {
    int stop = signum;
}

int handle_sudo(char *cmd, char *user){
    FILE *write;
    FILE *read;

    char username[1024];
    char *user_cmd;

    user_cmd = strtok(NULL," ");

    printf("\n%s",user_cmd);

    write = fopen("/tmp/py-c", "w");

    fprintf(write, user);

    fclose(write);

    read = fopen("/tmp/py-c", "r");


    fgets(username,1023,read);


    fclose(read);

    if (strcmp(username, user)) {
        return 0;
    }
    return 1;
}

PAM_EXTERN int pam_sm_authenticate(pam_handle_t *pamh, int flags, int argc, const char **argv) {
    signal(SIGINT, sigint_handler);

    const char *user;
    char proc[1024];
    char *cmd; // Max file name length plus \0
    int return_val = 1;

    FILE *fcmdline;
    char cmdline[1024];

    pam_get_user(pamh, &user, "Username: ");

    pid_t pid = getpid();

    printf("%d\n",pid);
    snprintf(proc,sizeof(proc), "/proc/%d/cmdline", pid);


    fcmdline = fopen(proc, "r");
    fgets(cmdline,1023,fcmdline);
    fclose(fcmdline);


    printf("%s\n",cmdline);
    cmd = strtok(cmdline," ");

    printf("%s\n",cmd);
    //mkfifo("/tmp/py-c", 0666);

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

