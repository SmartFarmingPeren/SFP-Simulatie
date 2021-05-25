using System.Collections.Generic;
using Unity.Robotics.ROSTCPConnector.MessageGeneration;


namespace RosMessageTypes.Moveit
{
    public class MoveGroupAction : Action<MoveGroupActionGoal, MoveGroupActionResult, MoveGroupActionFeedback, MoveGroupGoal, MoveGroupResult, MoveGroupFeedback>
    {
        public const string RosMessageName = "moveit_msgs/MoveGroupAction";

        public MoveGroupAction() : base()
        {
            this.action_goal = new MoveGroupActionGoal();
            this.action_result = new MoveGroupActionResult();
            this.action_feedback = new MoveGroupActionFeedback();
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
