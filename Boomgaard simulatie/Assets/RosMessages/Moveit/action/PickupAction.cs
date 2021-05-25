using System.Collections.Generic;
using Unity.Robotics.ROSTCPConnector.MessageGeneration;


namespace RosMessageTypes.Moveit
{
    public class PickupAction : Action<PickupActionGoal, PickupActionResult, PickupActionFeedback, PickupGoal, PickupResult, PickupFeedback>
    {
        public const string RosMessageName = "moveit_msgs/PickupAction";

        public PickupAction() : base()
        {
            this.action_goal = new PickupActionGoal();
            this.action_result = new PickupActionResult();
            this.action_feedback = new PickupActionFeedback();
        }

        public override List<byte[]> SerializationStatements()
        {
            var listOfSerializations = new List<byte[]>();
            listOfSerializations.AddRange(this.action_goal.SerializationStatements());
            listOfSerializations.AddRange(this.action_result.SerializationStatements());
            listOfSerializations.AddRange(this.action_feedback.SerializationStatements());

            return listOfSerializations;
        }

        public override int Deserialize(byte[] data, int offset)
        {
            offset = this.action_goal.Deserialize(data, offset);
            offset = this.action_result.Deserialize(data, offset);
            offset = this.action_feedback.Deserialize(data, offset);

            return offset;
        }

    }
}
