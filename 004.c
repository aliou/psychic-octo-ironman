#include <fcntl.h>
#include <sys/types.h>
#include <sys/uio.h>
#include <stdio.h>
#include <unistd.h>

const char *file = "files/rosalind_hamm.txt";

int main()
{
  int fd, ch_read, i = 0, hamm = 0;
  char buffer[4096];
  char *s, *t;

  if ((fd = open(file, O_RDONLY)) == -1)
  {
    printf("Error while opening the file.\n");
    return (1);
  }
  if ((ch_read = read(fd, buffer, 4095)) == -1)
  {
    printf("Error while reading the file.\n");
    close(fd);
    return (1);
  }
  buffer[ch_read] = 0;
  s = buffer;
  while (buffer[i] != ' ')
    i++;
  buffer[i] = 0;
  t = buffer + i + 1;

  i = 0;
  while (s[i] != 0)
  {
    if (s[i] != t[i])
      hamm++;
    i++;
  }

  printf("Hamming distance: %d.\n", hamm);
  return (0);
}
