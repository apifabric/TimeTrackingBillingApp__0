import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { PersonHomeComponent } from './home/Person-home.component';
import { PersonNewComponent } from './new/Person-new.component';
import { PersonDetailComponent } from './detail/Person-detail.component';

const routes: Routes = [
  {path: '', component: PersonHomeComponent},
  { path: 'new', component: PersonNewComponent },
  { path: ':id', component: PersonDetailComponent,
    data: {
      oPermission: {
        permissionId: 'Person-detail-permissions'
      }
    }
  },{
    path: ':person_id/Timesheet', loadChildren: () => import('../Timesheet/Timesheet.module').then(m => m.TimesheetModule),
    data: {
        oPermission: {
            permissionId: 'Timesheet-detail-permissions'
        }
    }
}
];

export const PERSON_MODULE_DECLARATIONS = [
    PersonHomeComponent,
    PersonNewComponent,
    PersonDetailComponent 
];


@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class PersonRoutingModule { }