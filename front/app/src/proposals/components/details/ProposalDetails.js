import ProposalDetailsController from './ProposalDetailsController'

export default {
  name : 'proposalDetails',
  config : {
    bindings         : {  selected: '<' },
    templateUrl      : 'src/proposals/components/details/ProposalDetails.html',
    controller       : [ '$mdBottomSheet', '$log', ProposalDetailsController ]
  }
};