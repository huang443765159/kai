# void FastRangingTest(void)
# {
#      uint8_t firstTimeInterrupt = 1;
#      static VL53L1_RangingMeasurementData_t RangingData;
#      status = VL53L1_WaitDeviceBooted(Dev);
#      status = VL53L1_DataInit(Dev);
#      status = VL53L1_StaticInit(Dev);
#      /* (1) Three important functions to use to configure the sensor in fast mode */
#      status = VL53L1_SetPresetMode(Dev, VL53L1_PRESETMODE_LITE_RANGING);
#      status = VL53L1_SetDistanceMode(Dev, VL53L1_DISTANCEMODE_SHORT);
#      status = VL53L1_SetMeasurementTimingBudgetMicroSeconds(Dev, 10000);
#      status = VL53L1_StartMeasurement(Dev);
#      do {
#           status = VL53L1_WaitMeasurementDataReady(Dev)
#           if(firstTimeInterrupt == 0){
#                status = VL53L1_GetRangingMeasurementData(Dev,&RangingData);
#                status = VL53L1_ClearInterruptAndStartMeasurement(Dev);
#           }
#           /* (2) If first interrupt, do not get data, clear interrupt and start */
#           else{
#               status = VL53L1_ClearInterruptAndStartMeasurement(Dev);
#               firstTimeInterrupt = 0;
#           }
# }
# while (1); }
