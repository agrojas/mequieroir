// Load the custom app ES6 modules

import ProposalsDataService from 'src/proposals/services/ProposalsDataService';

import ProposalsList from 'src/proposals/components/list/ProposalsList';
import ProposalDetails from 'src/proposals/components/details/ProposalDetails';



// Define the Angular 'proposals' module

export default angular
  .module("proposals", ['ngMaterial'])

  .component(ProposalsList.name, ProposalsList.config)
  .component(ProposalDetails.name, ProposalDetails.config)

  .service("ProposalsDataService", ProposalsDataService);
