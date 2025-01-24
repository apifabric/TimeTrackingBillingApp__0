import { Component, ViewEncapsulation } from '@angular/core';

@Component({
  selector: 'transactions-card',
  templateUrl: './Invoice-card.component.html',
  styleUrls: ['./Invoice-card.component.scss'],
  encapsulation: ViewEncapsulation.None,
  host: {
    '[class.Invoice-card]': 'true'
  }
})

export class InvoiceCardComponent {


}