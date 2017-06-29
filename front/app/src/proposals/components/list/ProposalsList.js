// Notice that we do not have a controller since this component does not
// have any specialized logic.


export default {
  name : 'proposalsList',
  config : {
    bindings         : {  proposals: '<', selected : '<', showDetails : '&onSelected' },
    templateUrl      : 'src/proposals/components/list/ProposalsList.html'
  }
};
