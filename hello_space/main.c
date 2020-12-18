#include "myriota_user_api.h"

time_t HelloSpace() {
  static uint16_t sequence_number;
  char message[MAX_MESSAGE_SIZE] = {0};
  sprintf(message, "%04d 425", sequence_number++);
  ScheduleMessage((uint8_t *)message, sizeof(message));
  return ASAP();
}

void AppInit() { ScheduleJob(HelloSpace, ASAP()); }
