import {CUSTOM_ELEMENTS_SCHEMA, NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { OntimizeWebModule } from 'ontimize-web-ngx';
import { SharedModule } from '../../shared/shared.module';
import  {INVOICE_MODULE_DECLARATIONS, InvoiceRoutingModule} from  './Invoice-routing.module';

@NgModule({

  imports: [
    SharedModule,
    CommonModule,
    OntimizeWebModule,
    InvoiceRoutingModule
  ],
  declarations: INVOICE_MODULE_DECLARATIONS,
  exports: INVOICE_MODULE_DECLARATIONS,
  schemas: [CUSTOM_ELEMENTS_SCHEMA]
})
export class InvoiceModule { }