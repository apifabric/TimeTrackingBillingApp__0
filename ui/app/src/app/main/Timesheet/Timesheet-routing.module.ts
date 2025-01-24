import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { TimesheetHomeComponent } from './home/Timesheet-home.component';
import { TimesheetNewComponent } from './new/Timesheet-new.component';
import { TimesheetDetailComponent } from './detail/Timesheet-detail.component';

const routes: Routes = [
  {path: '', component: TimesheetHomeComponent},
  { path: 'new', component: TimesheetNewComponent },
  { path: ':id', component: TimesheetDetailComponent,
    data: {
      oPermission: {
        permissionId: 'Timesheet-detail-permissions'
      }
    }
  }
];

export const TIMESHEET_MODULE_DECLARATIONS = [
    TimesheetHomeComponent,
    TimesheetNewComponent,
    TimesheetDetailComponent 
];


@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class TimesheetRoutingModule { }