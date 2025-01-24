import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { InvoiceHomeComponent } from './home/Invoice-home.component';
import { InvoiceNewComponent } from './new/Invoice-new.component';
import { InvoiceDetailComponent } from './detail/Invoice-detail.component';

const routes: Routes = [
  {path: '', component: InvoiceHomeComponent},
  { path: 'new', component: InvoiceNewComponent },
  { path: ':id', component: InvoiceDetailComponent,
    data: {
      oPermission: {
        permissionId: 'Invoice-detail-permissions'
      }
    }
  },{
    path: ':invoice_id/Payment', loadChildren: () => import('../Payment/Payment.module').then(m => m.PaymentModule),
    data: {
        oPermission: {
            permissionId: 'Payment-detail-permissions'
        }
    }
},{
    path: ':invoice_id/Task', loadChildren: () => import('../Task/Task.module').then(m => m.TaskModule),
    data: {
        oPermission: {
            permissionId: 'Task-detail-permissions'
        }
    }
}
];

export const INVOICE_MODULE_DECLARATIONS = [
    InvoiceHomeComponent,
    InvoiceNewComponent,
    InvoiceDetailComponent 
];


@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class InvoiceRoutingModule { }