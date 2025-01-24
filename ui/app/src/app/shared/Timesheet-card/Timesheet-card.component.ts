import { Component, ViewEncapsulation } from '@angular/core';

@Component({
  selector: 'transactions-card',
  templateUrl: './Timesheet-card.component.html',
  styleUrls: ['./Timesheet-card.component.scss'],
  encapsulation: ViewEncapsulation.None,
  host: {
    '[class.Timesheet-card]': 'true'
  }
})

export class TimesheetCardComponent {


}