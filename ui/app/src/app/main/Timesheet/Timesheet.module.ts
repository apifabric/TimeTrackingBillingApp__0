import {CUSTOM_ELEMENTS_SCHEMA, NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { OntimizeWebModule } from 'ontimize-web-ngx';
import { SharedModule } from '../../shared/shared.module';
import  {TIMESHEET_MODULE_DECLARATIONS, TimesheetRoutingModule} from  './Timesheet-routing.module';

@NgModule({

  imports: [
    SharedModule,
    CommonModule,
    OntimizeWebModule,
    TimesheetRoutingModule
  ],
  declarations: TIMESHEET_MODULE_DECLARATIONS,
  exports: TIMESHEET_MODULE_DECLARATIONS,
  schemas: [CUSTOM_ELEMENTS_SCHEMA]
})
export class TimesheetModule { }