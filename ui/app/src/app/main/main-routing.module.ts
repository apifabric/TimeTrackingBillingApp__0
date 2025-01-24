import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';

import { MainComponent } from './main.component';

export const routes: Routes = [
  {
    path: '', component: MainComponent,
    children: [
        { path: '', redirectTo: 'home', pathMatch: 'full' },
        { path: 'about', loadChildren: () => import('./about/about.module').then(m => m.AboutModule) },
        { path: 'home', loadChildren: () => import('./home/home.module').then(m => m.HomeModule) },
        { path: 'settings', loadChildren: () => import('./settings/settings.module').then(m => m.SettingsModule) },
      
    
        { path: 'Client', loadChildren: () => import('./Client/Client.module').then(m => m.ClientModule) },
    
        { path: 'Invoice', loadChildren: () => import('./Invoice/Invoice.module').then(m => m.InvoiceModule) },
    
        { path: 'Payment', loadChildren: () => import('./Payment/Payment.module').then(m => m.PaymentModule) },
    
        { path: 'Person', loadChildren: () => import('./Person/Person.module').then(m => m.PersonModule) },
    
        { path: 'Project', loadChildren: () => import('./Project/Project.module').then(m => m.ProjectModule) },
    
        { path: 'Task', loadChildren: () => import('./Task/Task.module').then(m => m.TaskModule) },
    
        { path: 'Timesheet', loadChildren: () => import('./Timesheet/Timesheet.module').then(m => m.TimesheetModule) },
    
    ]
  }
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class MainRoutingModule { }