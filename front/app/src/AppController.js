/**
 * Main App Controller for the Angular Material Starter App
 * @param ProposalsDataService
 * @param $mdSidenav
 * @constructor
 */
function AppController(ProposalsDataService, $mdSidenav) {
  var self = this;

  self.selected     = null;
  self.proposals        = [ ];
  self.selectProposal   = selectProposal;
  self.toggleList   = toggleProposalsList;

  // Load all registered users

  ProposalsDataService
        .loadAllProposals()
        .then( function( proposals ) {
          console.log(proposals);
          self.proposals    = [].concat(proposals);
          self.selected = proposals[0];
        });

  // *********************************
  // Internal methods
  // *********************************

  /**
   * Hide or Show the 'left' sideNav area
   */
  function toggleProposalsList() {
    $mdSidenav('left').toggle();
  }

  /**
   * Select the current avatars
   * @param menuId
   */
  function selectProposal ( proposal ) {
    self.selected = angular.isNumber(proposal) ? $scope.proposals[proposal] : proposal;
  }
}

export default [ 'ProposalsDataService', '$mdSidenav', AppController ];
