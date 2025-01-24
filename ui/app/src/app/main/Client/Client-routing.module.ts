import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { ClientHomeComponent } from './home/Client-home.component';
import { ClientNewComponent } from './new/Client-new.component';
import { ClientDetailComponent } from './detail/Client-detail.component';

const routes: Routes = [
  {path: '', component: ClientHomeComponent},
  { path: 'new', component: ClientNewComponent },
  { path: ':id', component: ClientDetailComponent,
    data: {
      oPermission: {
        permissionId: 'Client-detail-permissions'
      }
    }
  },{
    path: ':client_id/Person', loadChildren: () => import('../Person/Person.module').then(m => m.PersonModule),
    data: {
        oPermission: {
            permissionId: 'Person-detail-permissions'
        }
    }
},{
    path: ':client_id/Project', loadChildren: () => import('../Project/Project.module').then(m => m.ProjectModule),
    data: {
        oPermission: {
            permissionId: 'Project-detail-permissions'
        }
    }
}
];

export const CLIENT_MODULE_DECLARATIONS = [
    ClientHomeComponent,
    ClientNewComponent,
    ClientDetailComponent 
];


@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class ClientRoutingModule { }